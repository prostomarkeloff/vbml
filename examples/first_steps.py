from vbml import Pattern

pattern = Pattern("i am <name> i love <item>")
result = pattern.parse("i am vasya i love icecream")

print("Match succeed", result)
print("Match data", pattern.dict())
