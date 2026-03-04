

--TODO add words list, fix it repeating twice and implement the rest

local wordList = require("words")


local response_table = {
	is_letter = "Nice!\n",
	is_not_letter = "Try again!\n",
	game_start = "Guess the letters for this word!\n",
	game_end = "Try again next time!\n",
	letter_said = "Letter has already been said!\n"
}


	--Functon for checking a table for a certain characters (returns true or false)
	local function table_contains(character, table)
		for i,v in pairs(table) do
			if v == character then
				return true
			else
				return false
			end
		end
	end

	--Function for handling the guesses and game logic
	local function guess(tries, word, letters_table)

	local response = io.read(1) --Read one character from user input

	if tries > 0 then
		local response_lower = string.lower(response)

		--If the letter inputed is the same and not aleardy said then add it to the letters used table and print a W result
		if string.match(string.lower(word), response_lower) and not table_contains(response_lower, letters_table) then

			table.insert(letters_table, response_lower)
			print (response_table.is_letter)

			print(tries)

		elseif not string.match(string.lower(word), response_lower) then -- If letter doesnt MATCH and hasn't already been said


			print(response_table.is_not_letter)
			table.insert(letters_table, response_lower)

			guess(tries - 1, word, letters_table)

		else --If letter has already been said
			print(response_table.letter_said)
			end
		else -- If tries = 0
			print(response_table.game_end)
			return nil
		end


	guess(tries, word, letters_table)

end




function main()
	local currentWord = wordList[math.random(1, #wordList)] -- wordList is the file words, returns a table with words

	io.write(response_table.game_start .. "The word is " .. string.len(currentWord) .. " letters long\n")

	local letters_used = {}
	local num_of_tries = 5


guess(num_of_tries, currentWord, letters_used)

end



main()
