from project import main, loading, btc_price, bubble_text, clear_bubble_text, move_cursor_up

def test_main():
    main("hello", 2)
    main("world", 1.5)

def test_loading():
    loading()

def test_btc_price():
    price = btc_price()
    print(f"{price}")

def test_bubble_text():
    message = "hello"
    bubble = bubble_text(message)
    print(bubble)

def test_clear_bubble_text():
    global previous_bubble_lines
    previous_bubble_lines = 3
    clear_bubble_text()

def test_move_cursor_up():
    move_cursor_up(2)
