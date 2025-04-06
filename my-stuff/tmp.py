from great_tables import GT, style, loc, exibble

GT(exibble)


GT(
    exibble, 
    rowname_col = "row",
    groupname_col = "group"
).tab_header(title = "My Title")


GT(
    exibble, 
    rowname_col = "row",
    groupname_col = "group"
).tab_spanner(
    columns = ["date", "time", "datetime"],
    label = "A dance as old as time"
)

GT(
    exibble
).fmt_currency(
    columns = "currency",
    currency = "EUR",
    scale_by = 1_000_000
)

GT(
    exibble,
    rowname_col = "row"
).tab_style(
    style = style.fill(color = "lightblue"),
    locations = loc.body(columns = "num")
)

GT(
    exibble,
    rowname_col = "row"
).