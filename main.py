# GOAL: Create Web based GUI app to do the Problem Solving Questions
# Exercise by Tony Robbins
# The user is prompted to answer the questions and has the possibility of
# saving it locally to txt file
# OPTION: create database [Sqlite3, or TinyDb]


from nicegui import ui

app_name_label_mk = "# Problem Solving Questions"
tony_robbins_mk = "### by Tony Robbins"

ui.markdown(app_name_label_mk).classes(
    "h-60 w-60 bg-gradient-to-r from-red-100 to-blue-300 p-5"
)
ui.markdown(tony_robbins_mk)
ui.image(
    "https://www.usmagazine.com/wp-content/uploads/2019/04/Tony-Robbins-25-Things-You-Dont-Know-About-Me.jpg?quality=47&strip=all"
).classes("w-32")


ui.link("Made with <3 by Gero Zayas", "https://www.gerozayas.com")

ui.run()
