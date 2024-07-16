import dash
import re
import pandas as pd
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

catalog = pd.read_csv("catalog.csv")
catalog = catalog[catalog['sold_out'] == 'No']

app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
    )

#------------------
#>>>---LAYOUT---<<<
#------------------
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavbarBrand(
                            "COELHO Library",
                            style = {
                                'text-align': 'center',
                                'font-size': '250%',
                                'font-weight': 'bold',
                                'font-family': 'Times New Roman'
                            })
                    )
                ]
            )
        ]
    )
)

introduction = html.Div(
    dbc.Container(
        dbc.Card(
            dbc.Row([
                dbc.Col(
                    dbc.CardBody(
                        dbc.Carousel(
                            items = [
                                {
                                    'key': x, 
                                    'src': f'assets/my_photos/rafael00{x}.jpeg',
                                    } for x in range(1,5)
                            ],
                            controls = True,
                            indicators = True,
                            interval = 3000,
                            style = {'width': '100%', 'text-align': 'center'},
                            variant = 'dark'         
                        )
                    ), 
                    className = "col-md-4"
                ),
                dbc.Col(
                    dbc.CardBody([
                        html.P("""
Bem-vindo(a) à COELHO Library! Eu sou o Rafael, e criei esta página 
com o intuito de vender diversos livros que comprei nos últimos meses,
mas que não terei tempo para ler por questões pessoais e profissionais.""", 
                        className = "card-text",
                        style = {'font-size': '110%'}),
                        html.Br(),
                        html.P("""
Decidi vender a maioria dos livros que estão sem nenhuma (ou quase nenhuma) marca de uso por 50%
do valor original. São livros nas seguintes categorias: Desenvolvimento pessoal,
Ciência, Ficção, Comunicação, Marketing Digital, História, Biografia, Negócios e
Mercado Financeiro.""", 
                        className = "card-text",
                        style = {'font-size': '110%'}),
                        html.Br(),
                        html.P("""
Os livros disponíveis estão à venda APENAS para quem mora em Curitiba e Região Metropolitana. 
Para adquirí-los, é necessário combinar detalhes através de contato pelo WhatsApp. 
Clique no botão abaixo para saber mais e para comprar livros.""", 
                        className = "card-text",
                        style = {'font-size': '110%', 'font-weight': 'bold'}),
                        dbc.Button(
                            "Quero saber mais / Quero comprar livros",
                            color = "success",
                            style = {
                                'width': '100%'
                                },
                            href = "https://api.whatsapp.com/send/?phone=5541996234222&text=Ol%C3%A1+Rafael,+quero+saber+mais+informa%C3%A7%C3%B5es+sobre+os+livros+que+voc%C3%AA+est%C3%A1+vendendo.",
                            external_link = True
                        ),
                        html.Br(),
                        html.Br(),
                        html.P("""
Aproveitando a oportunidade, também quero convidar você a conhecer minha carreira
e meus projetos profissionais. Trabalho há mais de quatro anos nas áreas de Ciência de Dados,
Inteligência Artificial, Visão Computacional e Cybersecurity, e nos últimos meses venho
desenvolvendo um portfólio de projetos profissionais robustos, visando atingir o mercado
internacional nos próximos anos.""", 
                        className = "card-text",
                        style = {'font-size': '110%'}),
                        dbc.Row([
                            dbc.Col(
                                dbc.Button(
                                    "Portfólio Profissional - Rafael Coelho",
                                    color = "secondary",
                                    style = {
                                        'width': '100%'
                                        },
                                    href = "https://linktr.ee/__rafael__coelho__",
                                    external_link = True
                                ),
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "LinkedIn - Rafael Coelho",
                                    color = "secondary",
                                    style = {
                                        'width': '100%'
                                        },
                                    href = "https://linkedin.com/in/rafaelcoelho1409/",
                                    external_link = True
                                ),
                            )
                        ])
                    ], 
                    ),
                    className="col-md-8"
                )
            ])
        )
    )
)

filters = html.Div(dbc.Container([
    html.Hr(),
    dbc.Alert(
        "LIVROS", 
        color = "primary",
        style = {
            'text-align': 'center',
            'font-size': '150%',
            'font-weight': 'bold',
            'font-family': 'Times New Roman'
        }),
    dbc.Row([
        dbc.Col("Buscar"),
        dbc.Col("Seller"),
        dbc.Col("Categoria"),
        dbc.Col("Preço Mínimo (R$)"),
        dbc.Col("Preço Máximo (R$)")
    ],
    style = {
        'font-weight': 'bold',
    }),
    dbc.Row([
        dbc.Col(
            dcc.Input(
                value = "",
                type = "text",
                id = "filter_search",
                style = {'width': '100%'}
            )),
        dbc.Col(
            dcc.Dropdown(
                catalog["seller"].unique().tolist(),
                catalog["seller"].unique().tolist(),
                multi = True,
                id = "filter_seller"
            )),
        dbc.Col(
            dcc.Dropdown(
                catalog["genre"].unique().tolist(),
                catalog["genre"].unique().tolist(),
                multi = True,
                id = "filter_genre"
            )),
        dbc.Col(
            dcc.Input(
                min = catalog['price_discount'].min(),
                max = catalog['price_discount'].max(),
                step = 0.01,
                value = catalog['price_discount'].min(),
                type = "number",
                id = "filter_min_price",
                style = {'width': '100%'}
            )),
        dbc.Col(
            dcc.Input(
                min = catalog['price_discount'].min(),
                max = catalog['price_discount'].max(),
                step = 0.01,
                value = catalog['price_discount'].max(),
                type = "number",
                id = "filter_max_price",
                style = {'width': '100%'}
            ))
    ]),
    html.Hr()
], 
    #style = {'margin': '10px'},
    id = "filters_id"))

books = html.Div(id = "books_id")

app.layout = html.Div(
    children = [
        navbar,
        introduction,
        filters,
        books
    ]
)

#---------------------
#>>>---CALLBACKS---<<<
#---------------------

@app.callback(
    Output("books_id", "children"),
    Input("filter_search", "value"),
    Input("filter_seller", "value"),
    Input("filter_genre", "value"),
    Input("filter_min_price", "value"),
    Input("filter_max_price", "value"),
)
def filter_data(
    search,
    seller, 
    genre, 
    min_price, 
    max_price
    ):
    global catalog
    catalog = pd.read_csv("catalog.csv")
    catalog = catalog[catalog['sold_out'] == 'No']
    search = re.sub(r'[^A-Za-z0-9]', '', search)
    if search != "":
        catalog = catalog[
            (catalog['name'].str.contains(search, case = False)
             |
             catalog['author'].str.contains(search, case = False)
             |
             catalog['genre'].str.contains(search, case = False))]
    catalog = catalog[catalog['seller'].isin(seller)]
    catalog = catalog[catalog['genre'].isin(genre)]
    catalog = catalog[catalog['price_discount'] >= min_price]
    catalog = catalog[catalog['price_discount'] <= max_price]
    books = dbc.Container([
    dbc.CardGroup([
        dbc.Card([
            dbc.Row([
                dbc.Col([
                    dbc.CardBody([
                        dbc.Carousel(
                            items = [
                                {
                                    'key': '1', 
                                    'src': f'assets/{x}1.png',
                                    },
                                {
                                    'key': '2', 
                                    'src': f'assets/{x}2.png',
                                    },
                            ],
                            controls = True,
                            indicators = True,
                            interval = 3000,
                            style = {'width': '100%'},
                            variant = 'dark'
                        )])]),
                dbc.Col([
                    html.P(
                        catalog[catalog['filename'] == x]['name'],
                        style = {
                            'font-weight': 'bold',
                            'font-size': '125%'
                        }
                    ),
                    html.I(
                        catalog[catalog['filename'] == x]['author'],
                        style = {
                            'font-size': '100%'
                        }
                    ),
                    html.P(
                        catalog[catalog['filename'] == x]['genre'],
                        style = {
                            'font-size': '100%'
                        }
                    ),
                    html.Hr(),
                    html.P(
                        catalog[catalog['filename'] == x]['price_description'],
                        style = {
                            'font-weight': 'bold',
                            'font-size': '100%',
                        }
                    ),
                    html.P(
                        f'R${catalog[catalog["filename"] == x]["price_discount"].iloc[0]:.2f}',
                        style = {
                            'font-weight': 'bold',
                            'font-size': '200%',
                            'color': 'green'
                        }
                    ),
                    html.Hr(),
                    html.P(
                        'Preço original - ' + catalog[catalog['filename'] == x]['seller'],
                        style = {
                            'font-weight': 'bold',
                            'font-size': '100%',
                        }
                    ),
                    html.P(
                        f'R${catalog[catalog["filename"] == x]["price"].iloc[0]:.2f}',
                        style = {
                            'font-weight': 'bold',
                            'font-size': '200%',
                            'color': 'red'
                        }
                    ),
                    html.Div(
                        dbc.Row([
                            dbc.Col(
                                dbc.Button(
                                    "Detalhes",
                                    id = f"details_{x}",
                                    color = "success",
                                    style = {
                                        'margin': '10px',
                                        'width': '90%'},
                                    href = f"assets/{x}.pdf",
                                    external_link = True
                                ),
                            )
                        ]))])
                        
                ])
            ],
            style = {'margin': '5px'},
            outline = True) for x in catalog['filename'][y:y + 2]
        ]) for y in list(range(len(catalog)))[::2]
    ])
    return books


if __name__ == '__main__':
    app.run(debug = True)