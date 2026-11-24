class Question:
    
    def __init__(self, question_id, category, difficulty, prompt, choices, correct_answer):
        self.question_id = question_id
        self.category = category
        self.difficulty = difficulty
        self.prompt = prompt
        self.choices = choices
        self.correct_answer = correct_answer
        
    def answer_checking(self, answer):
        if answer.upper() == self.correct_answer:
             return True
        else: 
            return False

    
question_bank = {
    "HIST001": Question(
        question_id="HIST001",
        category="History",
        difficulty="Easy",
        prompt="Who was the first Roman emperor?",
        choices={
            "A": "Julius Caesar",
            "B": "Augustus",
            "C": "Nero",
            "D": "Marcus Aurelius"
        },
        correct_answer="B"
    ),

    "LIT001": Question(
        question_id="LIT001",
        category="Literature",
        difficulty="Medium",
        prompt="Who wrote the Divine Comedy",
        choices= {
            "A": "Geoffrey Chaucer",
            "B": "John Milton",
            "C": "Dante Alighieri",
            "D":"William Shakespeare"
        },
        correct_answer="C"
    ),

    "SPACE001": Question(
        question_id="SPACE001",
        category="Space & Astronomy",
        difficulty="Medium",
        prompt="Which planet is known as the Red Planet?",
        choices= {
            "A": "Venus",
            "B" : "Jupiter",
            "C" : "Mercury",
            "D": "Mars"
        },
        correct_answer="D"
    ),
    
    "HIST002": Question(
        question_id="HIST002",
        category="History",
        difficulty="Easy",
        prompt="In what year did the Battle of Hastings take place?",
        choices= {
            "A" : "1066",
            "B" : "1215",
            "C" :"1415",
            "D" : "1485"            
        },
        correct_answer="A"
    ),
    
    "LIT002": Question(
        question_id="LIT002",
        category="Literature",
        difficulty="Easy",
        prompt="Who wrote the novel Frankenstein?",
        choices= {
            "A" : "Jane Austen",
            "B" : "Mary Shelley",
            "C" :"Charlotte Brontë",
            "D" : "George Eliot"  
        },
        correct_answer="B"
    ),
    
    "PHIL001": Question(
        question_id="PHIL001",
        category="Philosophy",
        difficulty="Medium",
        prompt="Which ancient Greek philosopher wrote The Republic?",
        choices= {
            "A" : "Aristotle",
            "B" : "Socrates",
            "C" :"Plato",
            "D" : "Epicurus"            
        },
        correct_answer="C"
    ),
    
    "PHIL002": Question(
        question_id="PHIL002",
        category="Philosophy",
        difficulty="Hard",
        prompt="Which philosopher developed the concept of the categorical imperative?",
        choices= {
            "A" : "Friedrich Nietzsche",
            "B" : "David Hume",
            "C" :"John Locke",
            "D" : "Immanuel Kant"            
        },
        correct_answer="D"
    ),

    "SCI001": Question(
        question_id="SCI001",
        category="Science",
        difficulty="Easy",
        prompt="What process allows plants to convert sunlight into chemical energy?",
        choices= {
            "A" : "Photosynthesis",
            "B" : "Respiration",
            "C" :"Fermentation",
            "D" : "Transpiration"            
        },
        correct_answer="A"
    ),
     
    "SCI002": Question(
        question_id="SCI002",
        category="Science",
        difficulty="Medium",
        prompt="What is the SI unit used to measure force?",
        choices= {
            "A" : "Joule",
            "B" : "Newton",
            "C" :"Watt",
            "D" : "Pascal"            
        },
        correct_answer="B"
    ),
     
     "GEO001": Question(
        question_id="GEO001",
        category="Geography",
        difficulty="Easy",
        prompt="Which country has the largest land area in the world?",
        choices= {
            "A" : "Canada",
            "B" : "China",
            "C" :"Russia",
            "D" : "United States"            
        },
        correct_answer="C"
    ),
     
     "GEO002": Question(
        question_id="GEO002",
        category="Geography",
        difficulty="Medium",
        prompt="Which body of water separates Alaska from eastern Russia?",
        choices= {
            "A" : "Strait of Gibraltar",
            "B" : "Strait of Malacca",
            "C" :"Bosporus Strait",
            "D" : "Bering Strait"            
        },
        correct_answer="D"
    ),
     
        "SPACE002": Question(
        question_id="SPACE002",
        category="Space & Astronomy",
        difficulty="Hard",
        prompt="What is the name of the boundary surrounding a black hole beyond which nothing, including light, can escape?",
        choices= {
            "A" : "Event horizon",
            "B" : "Accretion disk",
            "C" :"Singularity",
            "D" : "Photon sphere"            
        },
        correct_answer="A"
    )
}

def get_questions_by_category(selected_category):
    filtered_questions = []
    for question in question_bank.values():
        if question.category == selected_category:
            filtered_questions.append(question)
    return filtered_questions

def get_questions_by_difficulty(selected_difficulty):
    filtered_questions = [] = []
    for question in question_bank.values():
        if question.difficulty == selected_difficulty:
            filtered_questions.append(question)
    return filtered_questions

def get_questions_by_category_and_difficulty(selected_category,selected_difficulty):
    filtered_questions = []
    for question in question_bank.values():
        if question.category == selected_category and question.difficulty == selected_difficulty:
            filtered_questions.append(question)
    return filtered_questions

def get_selected_questions(selected_category, selected_difficulty):
    if selected_category != "All":
        if selected_difficulty != "Mixed":
            return get_questions_by_category_and_difficulty(selected_category, selected_difficulty)
        else:
            return get_questions_by_category(selected_category)
    
    else:
        if selected_difficulty != "Mixed":
            return get_questions_by_difficulty(selected_difficulty)
        else:
            return  list(question_bank.values())
