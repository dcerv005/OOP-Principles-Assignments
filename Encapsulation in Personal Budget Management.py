#Question 1
#Task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name= category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category):
        self.__category_name = new_category
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):
        try :
            if new_budget > 0:
                self.__allocated_budget=new_budget
            else:
                raise ValueError("New Budget cannot be a negative number.")
        except Exception as e:
            print(f"\nError: {e}\n")
    def add_expenses(self, expense):
        if expense > self.__allocated_budget:
            raise ValueError("\nExpense is too high\n")
        else:
            self.set_allocated_budget((self.get_allocated_budget()-expense))

    def display_category_summary(self):
        print(f"Category: {self.get_category_name()} has a remaining budget of, ${self.get_allocated_budget()}")


food_category = BudgetCategory('Food', 500)
food_category.add_expenses(100)
food_category.display_category_summary()
food_category.set_allocated_budget(-10)
food_category.set_allocated_budget('100')
food_category.add_expenses(401)
            