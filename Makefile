
make:
	@python3 Overworld_main.py
	@make clean

clean:
	@rm -r __pycache__