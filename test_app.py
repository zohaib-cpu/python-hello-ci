from app import main

def test_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello World" in captured.out
