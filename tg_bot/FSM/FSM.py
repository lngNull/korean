from aiogram.fsm.state import State, StatesGroup

class GetLinck(StatesGroup):

        link = State()


class GetCarData(StatesGroup):

        price = State()
        engine_capacity = State()
        age = State()
        finally_state = State()

class FeedbackData(StatesGroup):

        model_car = State()
        budget = State()
        additional_parameters = State()
        contact = State()
        finally_state = State()

        # ====================

        username= State()
        full_name= State()
        # last_name= State()
