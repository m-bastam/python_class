# import all necessary libraries
from urllib import request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment


# graph results of top 7 words


def displayResults(words, site):

    count = [item[1] for item in words]
    word = [item[0] for item in words]
  
    plt.figure(figsize=(20, 10))  # define how large the figure appears
    plt.bar(word, count)
    plt.title(f"Analyzing Top Words from:{site[:50]}", fontname="Sans Serif", fontsize=14)
    plt.xlabel("Words", fontsize=20)
    plt.ylabel("# of Appearances", fontsize=14)
    plt.xticks(fontname="Sans Serif", fontsize=12)
    plt.yticks(fontname="Sans Serif", fontsize=12)
    plt.show()

# filter out all elements that do not contain text that appears on site


def filterTags(element):
    if element.parent.name in ["style", "script", "head", "title", "meta", "[document]"]:
        return False
    if isinstance(element, Comment):
        return False
    return True

# filter article words and hidden characters


def filterWaste(word):
    bad_words = ("the", "a", "in", "of", "to", "you", "\xa0", "and",
                 "at", "on", "for", "from", "is", "that", "his",
                 "are", "be", "-", "as", "&", "they", "with", "how",
                 "was", "her", "him", "i", "has", "|", "an", "or", "such", ".", "0", "1", "2", "3", "4")
    if word.lower() in bad_words:
        return False
    else:
        return True


def scrape(url_site):
    page = request.urlopen(url_site)
    soup = BeautifulSoup(page, 'html5lib')
    text = soup.find_all(text=True)     # will get all text within the document
    # The filter method is used to loop over every item within our text variable and apply
    # the filterTags function to know if the item should be included. We basically want to
    #  return True if the item is not a comment or element tag that shouldn’t be included.

    visible_text = filter(filterTags, text)
    # The filter() built-in function returns an iterator. the items are filtered through
    # a function to test if the item is accepted or not.
    # print('----------visible text:-------------')
    # print(text)
    word_count = {}
    for text in visible_text:
        words = text.replace("\n", "").replace("\t", "").split(" ")   # replace all hidden chars
        words = list(filter(filterWaste, words))
        for word in words:
            if word != "":       # if it doesn't equal an empty string
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    word_counts = sorted(word_count.items(),key=lambda kv: kv[1], reverse=True)   # sort on value
    return word_counts[:10]


# main part
try:
    # site = "https://www.farsnews.ir/"
    # site = "http://umz.ac.ir"
    site = "https://www.w3schools.com/"
    # site = "https://alansimpson.me/python/scrape_sample.html"
    # site = "https://www.microsoft.com/en-us/"
    # site = "https://docs.bigbluebutton.org/"
    print(site)
    top_words = scrape(site)
    top_word = top_words[0]    # tuple of (word, count)
    print(f"top_ words are : {top_words}")
    print("The top word is: {}".format(top_word[0]))
    displayResults(top_words, site)     # call to graph 
    
except Exception as e:
    print(e)
    print("Something went wrong, please try again.")

print("Thanks for analyzing! Come back again!")



