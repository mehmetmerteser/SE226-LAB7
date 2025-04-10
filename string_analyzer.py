

from string_package import reverse_string, capitalize_words, remove_punctuation
from string_package import count_characters, count_words, average_word_length

def main():
    s = input("Bir cümle girin: ")

    reversed_s = reverse_string(s)
    capitalized_s = capitalize_words(s)
    clean_s = remove_punctuation(s)

    print("\nTers hali:", reversed_s)
    print("Baş harfleri büyük:", capitalized_s)
    print("Noktalama işaretleri çıkarılmış:", clean_s)
    print("Karakter sayısı:", count_characters(clean_s))
    print("Kelime sayısı:", count_words(clean_s))
    print("Ortalama kelime uzunluğu:", average_word_length(clean_s))

if __name__ == "__main__":
    main()
