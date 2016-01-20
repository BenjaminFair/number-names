units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
big = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]
bigUnits = ["", "un", "duo", "tre", "quattuor", "quinqua", "se", "septe", "octo", "nove"]
bigUnitsSuffixTens = [
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "s", "s", "s", "s", "", "", "x", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "s", "s", "s", "s", "", "", "x", ""],
["", "n", "m", "n", "n", "n", "n", "n", "m", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "n", "m", "n", "n", "n", "n", "n", "m", ""]]
bigUnitsSuffixHundreds = [
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "x", "", "s", "s", "s", "", "", "x", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "x", "", "s", "s", "s", "", "", "x", ""],
["", "n", "n", "n", "n", "n", "n", "n", "m", ""],
["", "", "", "", "", "", "", "", "", ""],
["", "n", "n", "n", "n", "n", "n", "n", "m", ""]]
bigTens = ["", "dec", "vigint", "trigint", "quadragint", "quinquagint", "sexagint", "septuagint", "octogint", "nonagint"]
bigTensSuffix = ["", "i", "i" , "a", "a", "a", "a", "a", "a", "a"]
bigHundreds = ["", "cent", "ducent", "trecent", "quadringent", "quingent", "sescent", "septingent", "octingent", "nongent"]

def convert(number):
  if number < 0:
    return "negative " + convert(-number)
  elif number < 10:
    return convertUnits(number)
  elif number < 100:
    return convertTens(number)
  elif number < 1000:
    return convertHundreds(number)
  else:
    return convertBig(number)

def convertUnits(number):
  return units[number]
  
def convertTeens(number):
  return teens[number - 10]

def convertTens(number):
  if number < 20:
    return convertTeens(number)
  output = tens[number / 10]
  if number % 10 != 0:
    output += "-"
    output += convertUnits(number % 10)
  return output
  
def convertHundreds(number):
  output = convertUnits(number / 100)
  output += " hundred"
  if number % 100 != 0:
    output += " " + convert(number % 100)
  return output
  
def convertBig(number):
  output = ""
  if number % 1000:
    output = convert(number % 1000)
  number /= 1000
  count = 0
  while number != 0:
    if number % 1000:
      if output != "":
        output = convert(number % 1000) + " " + makeBig(count) + " " + output
      else:
        output = convert(number % 1000) + " " + makeBig(count)
    count += 1
    number /= 1000
  return output

def makeBig(index):
  if index < 10:
    return big[index]
  elif index < 100:
    return makeBigTens(index)
  elif index < 1000:
    return makeBigHundreds(index)
  else:
    return "*10^" + str((index + 1)*3) + " (No name)"

def makeBigTens(index):
  output = ""
  output += bigUnits[index % 10]
  output += bigUnitsSuffixTens[index % 10][index / 10]
  output += bigTens[index / 10] + "illion"
  return output
def makeBigHundreds(index):
  output = ""
  output += bigUnits[index % 10]
  if (index % 100) / 10 != 0:
    output += bigUnitsSuffixTens[index % 10][(index % 100) / 10]
    output += bigTens[(index % 100) / 10]
    output += bigTensSuffix[(index % 100) / 10]
  else:
    output += bigUnitsSuffixHundreds[index % 10][index / 100]
  output += bigHundreds[index / 100] + "illion"
  return output
