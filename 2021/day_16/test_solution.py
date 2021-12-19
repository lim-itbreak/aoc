from solution import *


def test_read_literal() -> None:
    expected: int = 2021
    packet: Packet = Packet()
    read_literal("101111111000101000", 0, packet)
    assert packet.literal == expected


def test_read_packet() -> None:
    expected: int
    packets: List[Packet] = []
    read_packet("110100101111111000101000", 0, packets)

    expected = 6
    assert packets[0].version == expected

    expected = 4
    assert packets[0].type_id == expected

    expected = 2021
    assert packets[0].literal == expected

    expected = 0
    assert len(packets[0].packets) == expected


def test_part1() -> None:
    expected: int

    expected = 16
    assert part1("8A004A801A8002F478") == expected

    expected = 12
    assert part1("620080001611562C8802118E34") == expected

    expected = 23
    assert part1("C0015000016115A2E0802F182340") == expected

    expected = 31
    assert part1("A0016C880162017C3686B18A3D4780") == expected


def test_part2() -> None:
    expected: int

    expected = 3
    assert part2("C200B40A82") == expected

    expected = 54
    assert part2("04005AC33890") == expected

    expected = 7
    assert part2("880086C3E88112") == expected

    expected = 9
    assert part2("CE00C43D881120") == expected

    expected = 1
    assert part2("D8005AC2A8F0") == expected

    expected = 0
    assert part2("F600BC2D8F") == expected

    expected = 0
    assert part2("9C005AC2F8F0") == expected

    expected = 1
    assert part2("9C0141080250320F1802104A08") == expected
