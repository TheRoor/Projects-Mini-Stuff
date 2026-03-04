
local numbers = require("dependencies.numbers_ascii")

local function match()
	local time = tostring(os.date("%S"))
	local return_table = {}


	for i,v in pairs(numbers) do
		for w in string.gmatch(time, i) do
			 table.insert(return_table,w)
		end
	end
	return return_table
end


function main()
	local time_ascii = match()
	local ascii_numbers_table = {}

	for i,v in pairs(time_ascii) do
		table.insert(ascii_numbers_table,tonumber(v))
	end


	for index, value in pairs(ascii_numbers_table) do
		for line = 1, #numbers[value], 1 do
			print(numbers[value][line])
		end
		io.write("\n")
	end
end

main()
