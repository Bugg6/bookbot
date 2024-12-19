

def main():
    def word_count(book: str) -> int:
        words = len(book.split())
        return words
    
    def number_of_characters(book: str) -> dict:
        character_dict = {}
        lowercase = book.lower()
        words = lowercase.split()
        for word in words:
            for char in word:
                if char.isalpha() and char in character_dict:
                    character_dict[char] += 1
                elif char.isalpha():
                    character_dict[char] = 1
        
        return character_dict


    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    def convert_dict_to_list_and_sort(characters: dict) -> list:
        def sort_on(dict):
            return dict["num"]
        result = []
        for key, value in characters.items():
            result.append({"character": key, "num": value})
        
        result.sort(reverse=True, key=sort_on)
        
        return result

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document", end="\n\n")

    for dicts in convert_dict_to_list_and_sort(number_of_characters(file_contents)):
        print(f"The {dicts["character"]} character was found {dicts["num"]} times", end="\n")
    
    print("--- End report ---")

    




main()