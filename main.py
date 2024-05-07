# GOAL: Create Web based GUI app to do the Problem Solving Questions
# Exercise by Tony Robbins
# The user is prompted to answer the questions and has the possibility of
# saving it locally to txt file
# OPTION: create database [Sqlite3, or TinyDb]


from nicegui import ui

app_name_label = "# Problem Solving Questions"
tony_robbins = "### by Tony Robbins"
gero_zayas_link = "Made with <3 by Gero Zayas"
gero_zayas_url = "https://www.gerozayas.com"


with ui.element("div").classes("p-1 bg-blue-100"):
    ui.label("inside a colored div")
    ui.markdown(app_name_label).classes(
        "h-60 w-60 bg-gradient-to-r from-red-100 to-blue-300 p-5"
    )
    ui.markdown(tony_robbins)
    ui.image(
        "https://www.usmagazine.com/wp-content/uploads/2019/04/Tony-Robbins-25-Things-You-Dont-Know-About-Me.jpg?quality=47&strip=all"
    ).classes("w-32")

    ui.link(gero_zayas_link, gero_zayas_url)

ui.run()
