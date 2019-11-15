from pyecharts import options as opts
from pyecharts.charts import Bar, Map, Page, Pie, Sankey, Timeline
from pyecharts.faker import Collector, Faker

C = Collector()


@C.funcs
def timeline_bar() -> Timeline:
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_pie() -> Timeline:
    attr = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        pie = (
            Pie()
            .add(
                "商家A",
                [list(z) for z in zip(attr, Faker.values())],
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(pie, "{}年".format(i))
    return tl


@C.funcs
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        map0 = (
            Map()
            .add(
                "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=200),
            )
        )
        tl.add(map0, "{}年".format(i))
    return tl


@C.funcs
def timeline_with_multi_axis() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_sankey() -> Timeline:
    tl = Timeline()
    names = ("商家A", "商家B", "商家C")
    nodes = [{"name": name} for name in names]
    for i in range(2015, 2020):
        links = [
            {"source": names[0], "target": names[1], "value": Faker.values()[0]},
            {"source": names[1], "target": names[2], "value": Faker.values()[0]},
        ]
        sankey = (
            Sankey()
            .add(
                "sankey",
                nodes,
                links,
                linestyle_opt=opts.LineStyleOpts(
                    opacity=0.2, curve=0.5, color="source"
                ),
                label_opts=opts.LabelOpts(position="right"),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年商店（A, B, C）营业额差".format(i))
            )
        )
        tl.add(sankey, "{}年".format(i))
    return tl


Page().add(*[fn() for fn, _ in C.charts]).render()
