from lib.diary_entry import DiaryEntry


'''
    Check __init__ loads:
'''

def test_init_setup_is_correct():
    de = DiaryEntry("Sports", "Bball, fball, pingpong, tennis")
    titleresult = de.title
    contentresult = de.contents
    assert titleresult == "Sports"
    assert contentresult == "Bball, fball, pingpong, tennis"

'''
    Diary Entry is formatted correctly:
'''

def test_entry_is_formatted_correctly():
    de = DiaryEntry("Sports", "Bball, fball, pingpong, tennis")
    result = de.format()
    assert result == "Sports: Bball, fball, pingpong, tennis"

'''
    Count and return the number of words 
    from the diary entry (contents).
'''

def test_from_diary_entry_return_number_of_words():
    de = DiaryEntry("Van Damme Movies", "Hard target, Cyborg, Double Impact, Kickboxer, AWOL")
    result = de.count_words()
    assert result == 7

'''
    Return an estimated reading time  
    for the words per minute (wpm) and content given.
'''

def test_return_estimated_reading_time_in_minutes():
    de = DiaryEntry("Happy Days", "The porch swing extends effortlessly and smooth, her feet just reaching over the withering edge of the deck boards, only to make its way backward with a crackling, obnoxious squeak. Her love, her very own Mr. Fix It, long since gone, spent many evenings oiling, adjusting, replacing rusted pieces, but the swing never recovered, the squealing never ceased. As with so many things that annoy the young, she had learned over time not to mind the sound. It took on a nostalgic quality. With each squeal, with each backward swing, she can see him, sweat lining his collar, his brow furrowed with confusion, with exasperation that the swing continued to defy him and now, in the early morning sunshine, it makes her smile On any regular Friday morning, she would be sitting here in preparation to welcome Joy, her home aide, who would bring an enormous cup of coffee and the morning paper. She liked hearing about Joy’s young children- their report cards, sporting events, summer activities- returning her to a time of life that felt eternally sweet, like the sun was always shining. But Joy also smelled a bit unpleasant and would plop her heavy frame onto the porch swing roughly, without regard for its memories. She felt sorry for the many faceless people all caught up in this global emergency but it was a little relieving Joy wouldn’t be over to disrespect the swing today One of the kids had installed a home phone with extra large buttons and a deafening ring that could probably be heard two houses over. She could hear it yelling now from the sideboard in the dining room as though it were inches from her ears which were less than functional these days. She chuckled, imagining what that ridiculous phone must sound like.")
    wpm = de.reading_time(200)
    assert wpm == "1.5 minutes to read."

'''
    Given the words per minute (wpm) to read
    And given the minutes allowed to read
    Return a suitable chunk of text
'''

def test_return_suitable_chunk_based_on_wpm_and_time_given():
    de = DiaryEntry("Happy Nights", "The porch swing extends effortlessly and smooth, her feet just reaching over the withering edge of the deck boards, only to make its way backward with a crackling, obnoxious squeak. Her love, her very own Mr. Fix It, long since gone, spent many evenings oiling, adjusting, replacing rusted pieces, but the swing never recovered, the squealing never ceased. As with so many things that annoy the young, she had learned over time not to mind the sound. It took on a nostalgic quality. With each squeal, with each backward swing, she can see him, sweat lining his collar, his brow furrowed with confusion, with exasperation that the swing continued to defy him and now, in the early morning sunshine, it makes her smile On any regular Friday morning, she would be sitting here in preparation to welcome Joy, her home aide, who would bring an enormous cup of coffee and the morning paper. She liked hearing about Joy’s young children- their report cards, sporting events, summer activities- returning her to a time of life that felt eternally sweet, like the sun was always shining. But Joy also smelled a bit unpleasant and would plop her heavy frame onto the porch swing roughly, without regard for its memories. She felt sorry for the many faceless people all caught up in this global emergency but it was a little relieving Joy wouldn’t be over to disrespect the swing today One of the kids had installed a home phone with extra large buttons and a deafening ring that could probably be heard two houses over. She could hear it yelling now from the sideboard in the dining room as though it were inches from her ears which were less than functional these days. She chuckled, imagining what that ridiculous phone must sound like.")
    r_chunk = de.reading_chunk(200,1)
    assert r_chunk == "The porch swing extends effortlessly and smooth, her feet just reaching over the withering edge of the deck boards, only to make its way backward with a crackling, obnoxious squeak. Her love, her very own Mr. Fix It, long since gone, spent many evenings oiling, adjusting, replacing rusted pieces, but the swing never recovered, the squealing never ceased. As with so many things that annoy the young, she had learned over time not to mind the sound. It took on a nostalgic quality. With each squeal, with each backward swing, she can see him, sweat lining his collar, his brow furrowed with confusion, with exasperation that the swing continued to defy him and now, in the early morning sunshine, it makes her smile On any regular Friday morning, she would be sitting here in preparation to welcome Joy, her home aide, who would bring an enormous cup of coffee and the morning paper. She liked hearing about Joy’s young children- their report cards, sporting events, summer activities- returning her to a time of life that felt eternally sweet, like the sun was always shining. But Joy also smelled a bit unpleasant and would plop her heavy frame onto the porch"