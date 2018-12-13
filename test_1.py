#easygui sample
import easygui as g
import PIL

g.ynbox('Shall I continue?', 'Title', ('Yes', 'No'), 'n.jpg')
g.msgbox('This is a basic message box.', 'Title Goes Here')
'OK'
g.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
'Chocolate'
