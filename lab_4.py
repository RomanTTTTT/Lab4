import random
def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        next(v)
        return v
    return wrapper

class MyDay:
    def __init__(self):
        self.start = self._create_start()
        self.eat = self._create_eat()
        self.sleep = self._create_sleep()
        self.go_for_a_walk = self._create_walk()
        self.end = self._create_end()
        self.study_in_ucu = self._create_ucu()
        self.study_at_home = self._create_home()
        self.relax = self._create_relax()
        
        self.current_state = self.start
        self.stopped = False

    def my_day_func(self, hour:int):
        print(f"My day, starting from {hour} o'clock")
        while self.current_state != self.end:
            print(f"Hour - {hour}")
            self.current_state.send(hour)
            hour += 1
    
    @prime
    def _create_start(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or cur_time < 6 or cur_time > 8:
                break
            oversleep_number = random.randint(1, 10)
            if oversleep_number == 1:
                print("ZZZzzZZZzZ")
                self.current_state = self.sleep # overslept
            else:
                print("Luckily, I woke up!")
                self.current_state = self.eat # woke up on time

            
    
    @prime
    def _create_sleep(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or cur_time < 0 or cur_time > 24:
                break
            if cur_time >= 8 and cur_time <= 9:
                oversleep_number = random.randint(1, 10)
                if oversleep_number == 1:
                    print("ZZZzzZZZzZ")
                    self.current_state = self.sleep
                else:
                    print("Gotta hurry up!")
                    self.current_state = self.study_in_ucu
            elif cur_time > 9 and cur_time <= 11:
                print("It seems I won`t be in time for class today")
                self.current_state = self.eat
            elif 6 >= cur_time >= 0:
                print("What a wonderful day was today! *yawns*")
                self.current_state = self.end
            else:
                break

    @prime
    def _create_eat(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or cur_time < 0 or cur_time > 24:
                break
            if cur_time >= 8 and cur_time <= 9:
                print("I woke up on time, so will get to UCU in time")
                self.current_state = self.study_in_ucu
            elif cur_time > 9 and cur_time <= 11:
                print("Well, time to relax~")
                self.current_state = self.relax
            elif 15 <= cur_time <= 16:
                rain_number = random.randint(1, 10)
                if rain_number <=3:
                    print("Oh no it`s raining! Guess I will relax at home then")
                    self.current_state = self.relax
                else:
                    print("What a great weather! I am going outside")
                    self.current_state = self.go_for_a_walk
            elif 23 <= cur_time <= 24:
                print("ZZZZzZZZzzZZ")
                self.current_state = self.sleep
            else:
                break

    @prime
    def _create_ucu(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or 9 >= cur_time or cur_time >= 12:
                break
            print("I will relax for a bit...")
            self.current_state = self.relax

    @prime
    def _create_relax(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or cur_time < 12 or cur_time > 20:
                break
            if 15 > cur_time >= 11:
                print("Time for lunch!")
                self.current_state = self.eat
            elif 20 > cur_time > 16:
                print("Ok lets do some homework")
                self.current_state = self.study_at_home
            else:
                break

    @prime
    def _create_home(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int):
                break
            if 12 >= cur_time > 9:
                print("Guess I have to learn everything myself")
                self.current_state = self.relax
            elif 20 <= cur_time < 23:
                print("Lets eat and go bed")
                self.current_state = self.eat
            else:
                break
    
    @prime
    def _create_walk(self):
        while True:
            cur_time = yield
            if not isinstance(cur_time, int) or 16 >= cur_time or cur_time >= 20:
                break
            print("Ok, lets go back and do our homework")
            self.current_state = self.study_at_home
    @prime
    def _create_end(self):
        while True:
            char = yield
            break
if __name__ == "__main__":
    hour = int(input())
    day = MyDay()
    day.my_day_func(hour)
