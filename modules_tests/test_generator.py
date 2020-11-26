from generator import CustomFloat32
from algorithm import merge_sort


def test_custom_float32_comp():
    a = CustomFloat32(1)
    b = CustomFloat32(2)
    c = CustomFloat32(3)
    d = CustomFloat32(3)
    e = CustomFloat32(4)

    assert a < b
    assert b > a
    assert c <= d
    assert d <= e
    assert c >= d
    assert e >= d
    assert c == d
    assert d != e
    assert a.effort == 1
    assert b.effort == 1
    assert c.effort == 3
    assert d.effort == 2
    assert e.effort == 1


def test_merge_w_custom_float32_comp():
    a = CustomFloat32(1)
    b = CustomFloat32(2)
    c = CustomFloat32(3)
    e = CustomFloat32(4)

    l = [e, b, c, a]
    merge_sort(l, 0, 3)

    effort_sum = 0
    for e in l:
        effort_sum += e.effort

    assert effort_sum == 5
