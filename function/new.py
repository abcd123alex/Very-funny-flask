from datetime import date

class new:
  def newfile(self):
    with open(f"data/{date.today()}.csv", "x") as file:
      file.close()
    with open(f"data/{date.today()}.csv", "a") as file:
      file.write("name, osis, organization\n")
      file.close()
    return

  def date(self):
    return date.today()

alex = new()

if __name__ == "__main__":
  alex.newfile()


