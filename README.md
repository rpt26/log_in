# log_in
A simple gui to record IDs as typed or from a card reader with the time.

This program uses PySimpleGui to open a window that will record IDs entered into an input element.

It will output a message confirming the time that the ID was recorded and it will write the ID and the time to a file for subsequent use.

It is very close to the cookbook examples for a persistent window, the main change is to the styling and 
to add the window.refresh() and small delay to make the feedback more human affirmative. There may be a
better way of achieving this, there is a small possibility of cards clashing in the 100 milliseconds it pauses.

This will get reviewedin case it does prove to be an issue.



