from faker import Faker #generate random text
import ipywidgets as widgets

#Label widget creator
def label_generator(name, width):
    return widgets.HTML(
        value=f"""
            <div style="
                font-family: Arial;
                font-size: 1rem;
                font-weight: 700;
                display: flex;
                width: 100%;
                height: 100%;
                padding: 10px;
            ">
                {name}
            </div>
        """,
        layout=widgets.Layout(
            width=f'{width}%',
            height='100%'
        )
    )

#Random text generator
def random_text_generator(level):
    fake = Faker("en_US")
    if level == 'easy':
        text = fake.sentence(nb_words=30)
    elif level == 'normal':
        text = fake.sentence(nb_words=70)
    elif level == 'hard':
        text = fake.sentence(nb_words=130)
    else:
        raise ValueError('Difficulty Level should only be easy, normal or hard.')

    return text