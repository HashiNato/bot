from aiogram.dispatcher.filters.state import StatesGroup, State

class States_w(StatesGroup):
    States_run = State()
    States_day = State()
    States_time = State()

class States_clear(StatesGroup):
    State_run_clear = State()
    States_user = State()
    States_close = State()
