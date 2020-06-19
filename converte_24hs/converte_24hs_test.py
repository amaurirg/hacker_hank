from converte_24hs.converte_24hs import converte_24hs


def test_converte_24hs():
    assert converte_24hs("09:13:45PM") == "21:13:45"
    assert converte_24hs("12:25:17PM") == "12:25:17"
    assert converte_24hs("07:22:15AM") == "07:22:15"
    assert converte_24hs("01:56:34AM") == "01:56:34"
    assert converte_24hs("05:18:56PM") == "17:18:56"
    assert converte_24hs("07:05:45PM") == "19:05:45"
    assert converte_24hs("12:40:22AM") == "00:40:22"
