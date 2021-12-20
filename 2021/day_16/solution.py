from math import prod
from typing import Dict, List, TextIO

Input = str


class Packet(object):
    def __init__(self) -> None:
        self.version: int = -1
        self.type_id: int = -1
        self.packets: List[Packet] = []
        self.literal: int = -1

    def sum_of_versions(self) -> int:
        return self.version + sum(packet.sum_of_versions() for packet in self.packets)

    def value(self) -> int:
        match self.type_id:
            case 0:
                return sum(packet.value() for packet in self.packets)
            case 1:
                return prod(packet.value() for packet in self.packets)
            case 2:
                return min(packet.value() for packet in self.packets)
            case 3:
                return max(packet.value() for packet in self.packets)
            case 4:
                return self.literal
            case 5:
                return int(self.packets[0].value() > self.packets[1].value())
            case 6:
                return int(self.packets[0].value() < self.packets[1].value())
            case 7:
                return int(self.packets[0].value() == self.packets[1].value())


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return fp.read()


def read_packet(data: str, bit: int, packets: List[Packet]) -> int:
    packet = Packet()
    packet.version = int(data[bit : bit + 3], 2)
    packet.type_id = int(data[bit + 3 : bit + 6], 2)
    bit += 6
    if packet.type_id == 4:
        bit = read_literal(data, bit, packet)
    else:
        bit = read_operator(data, bit, packet)
    packets.append(packet)
    return bit


def read_literal(data: str, bit: int, packet: Packet) -> int:
    literal: List[str] = []
    while True:
        literal.append(data[bit + 1 : bit + 5])
        if data[bit] == "0":
            break
        bit += 5
    packet.literal = int("".join(literal), 2)
    return bit + 5


def read_operator(data: str, bit: int, packet: Packet) -> int:
    match data[bit]:
        case "0":
            i_stop = bit + 16 + int(data[bit + 1 : bit + 16], 2)
            bit += 16
            while bit < i_stop:
                bit = read_packet(data, bit, packet.packets)
        case "1":
            n_packets = int(data[bit + 1 : bit + 12], 2)
            bit += 12
            for _ in range(n_packets):
                bit = read_packet(data, bit, packet.packets)
    return bit


def decode(transmission: Input) -> Packet:
    binary: Dict[str, str] = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    data: str = "".join(binary[_hex_] for _hex_ in transmission)
    packets: List[Packet] = []
    bit: int = 0
    while bit < len(data) and len(data) - bit > 10:
        bit = read_packet(data, bit, packets)
    return packets[0]


def part1(inputs: Input) -> int:
    return decode(inputs).sum_of_versions()


def part2(inputs: Input) -> int:
    return decode(inputs).value()


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
