def format_currency(val,symbol="Rs."):
  return f"{symbol} {val:.2f}"

def parse_input(prompt, cast_type=str):
  while True:
    try:
      raw=input(prompt).strip()
      if not raw:
        print("Input cannot be empty. Try again.")
        continue
      return cast_type(raw)
    except ValueError:
      print(f"Invalid input type. Expected {cast_type.__name__}.")

def log_event(*args,**kwargs):
  sep=kwargs.get("sep","|")
  msg=sep.join(str(a) for a in args)
  print(f"[LOG] {msg}")
