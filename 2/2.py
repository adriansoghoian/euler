# Answer = 4613732

last = 1 
temp = 1
current = 2
sum = 0

while current < 4000000:
		if current % 2 == 0:
			sum += current
		temp = last 
		last = current 
		current += temp 

print(sum)