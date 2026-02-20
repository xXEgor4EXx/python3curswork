from nicegui import ui, html

ui.label('some label')
ui.chat_message('Hello NiceGUI!',
                name='Robot',
                stamp='now',
                avatar='https://robohash.org/ui')
ui.mermaid('''
    graph LR;
        A --> B;
        A --> C;
''')
with ui.element('div').classes('p-2 bg-blue-100'):
    ui.label('inside a colored div')

with html.section().style('font-size: 120%'):
    html.strong('This is bold.') \
        .classes('cursor-pointer') \
        .on('click', lambda: ui.notify('Bold!'))
    html.hr()
    html.em('This is italic.').tooltip('Nice!')
    with ui.row():
        html.img().props('src=https://placehold.co/60')
        html.img(src='https://placehold.co/60')

with ui.fab('navigation', label='Transport'):
    ui.fab_action('train', on_click=lambda: ui.notify('Train'))
    ui.fab_action('sailing', on_click=lambda: ui.notify('Boat'))
    ui.fab_action('rocket', on_click=lambda: ui.notify('Rocket'))

with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
    badge = ui.badge('0', color='red').props('floating')

editor = ui.codemirror('print("Edit me!")', language='Python').classes('h-32')
ui.select(editor.supported_languages, label='Language', clearable=True) \
    .classes('w-32').bind_value(editor, 'language')
ui.select(editor.supported_themes, label='Theme') \
    .classes('w-32').bind_value(editor, 'theme')
ui.checkbox('Wrap Lines', value=editor.line_wrapping,
            on_change=lambda e: editor.set_line_wrapping(e.value))  
ui.run()