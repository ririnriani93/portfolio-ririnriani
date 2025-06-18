# Note: This version is modified for public portfolio.
# Some internal modules and configurations are hidden for confidentiality.

# Master item page : Input form for kitchen asset data

import dash
from dash import html, dcc, Input, Output, State, callback, no_update, clientside_callback
from dash.exceptions import PreventUpdate
from datetime import datetime

# External packages
import dash_mantine_components as dmc
from dash_labs.plugins import register_page

# Placeholder imports (internal functions and DB connection)
# from fn_umum import *       # Hidden for confidentiality
# from configdb import dbConnection
# from listquery import *

# Optional for authentication
# from flask_login import current_user

# SQLAlchemy and DB engine (optional usage)
from sqlalchemy import create_engine, insert, delete, update, text
from sqlalchemy.pool import NullPool


page = "item_asset"
register_page(__name__,
              title='Input Master Item Asset',
              order=104)

layout = html.Div([
    html.Div([
        dcc.Store(id=page+ '-ds_item'),
        dcc.Location(id=page+ '-url', refresh=True),
        html.H2('Input Master Item Asset',
                style={
                    'fontSize': 50,
                    'color': 'black',
                    'fontFamily': 'Dancing Script',
                    #'backgroundColor': '#ccffee',
                    'textAlign': 'center',
                    'marginBottom': '20px'
                }),
        dmc.Stack([
            dmc.ButtonGroup([
                dcc.Link(
                    dmc.Button(
                        "Master Item",
                        id=page+'master-item-btn',
                        variant="light",
                        color="blue",
                        style={'fontSize': '12px', 'padding': '4px 8px', 'marginTop': '20px',"width":"100%"}
                        ),
                    href='/master-item',  # Tautkan ke halaman master-item
                    style={'textDecoration': 'none'}
                ),       
                dcc.Link(
                    dmc.Button(
                        "Master Supplier",
                        id=page+'master-supplier',
                        variant="light",
                        color="blue",
                        style={'fontSize': '12px', 'padding': '4px 8px', 'marginTop': '20px',"width":"100%"}
                        ),
                    href='/master-supplier',  # Tautkan ke halaman master-item
                    style={'textDecoration': 'none'}
                ),
                dcc.Link(
                    dmc.Button(
                        "Master Item Supp",
                        id=page+'master-item-supp-btn',
                        variant="light",
                        color="blue",
                        style={'fontSize': '12px', 'padding': '4px 8px', 'marginTop': '20px',"width":"100%"}
                        ),
                    href='/master-item-supp',  # Tautkan ke halaman master-item
                    style={'textDecoration': 'none'}
                ),
                dcc.Link(
                    dmc.Button(
                        "Item Asset",
                        id=page+ 'item-asset-btn',
                        variant="light",
                        color="blue",
                        style={'fontSize': '12px', 'padding': '4px 8px', 'marginTop': '20px', 'textAlign': 'center', "width": "100%"}
                        ),
                    href='/item-asset',
                    style={'textDecoration': 'none'}
                ),
                        ],
                    ),
            
            html.Br(),
            dmc.Grid(
                children=[
                    dmc.GridCol(
                        children=[
                            dmc.Select(
                                label='Item Type',
                                id=page+ 'asset_item_type',
                                data=[
                                    {"label": "Electronics", "value": "E"},
                                    {"label": "Furniture", "value": "F"},
                                    {"label": "Kitchen Equipment", "value": "K"},
                                    {"label": "Office Supplies", "value": "O"},
                                ],
                                style={"marginBottom": "10px", "width": "100%"}
                            ),
                            dmc.TextInput(label="Item Code", id=page+ 'asset_item_code',  style={"marginBottom": "10px", "width": "100%"}, disabled=True),
                            dmc.TextInput(label="Item Name", id=page+ 'asset_item_name',  style={"marginBottom": "10px", "width": "100%"}),
                            dmc.TextInput(label="Item Brand", id=page+ 'asset_item_brand',  style={"marginBottom": "10px", "width": "100%"}),  
                            dmc.Select(
                                label='Item Unit',
                                id='asset_item_unit',
                                style={"marginBottom": "10px", "width": "100%"}
                            ),
                        ],
                        span=6
                    ),
                    dmc.GridCol(
                        children=[
                            dmc.TextInput(label="Item Size", id=page+ 'asset_item_size',  style={"marginBottom": "10px", "width": "100%"}),
                            dmc.TextInput(label="Item Price", id=page+ 'asset_item_price',  style={"marginBottom": "10px", "width": "100%"}),
                            dmc.TextInput(label="Item Discount", id=page+ 'asset_item_discount',  style={"marginBottom": "10px", "width": "100%"}),
                            dmc.Textarea(label="Item Note", id=page+ 'asset_item_note',  style={"marginBottom": "18px", "width": "100%"}),
                            dmc.Modal(
                                id=page+'-modal_tipe1',
                                title="Notification",
                                children=[],
                                centered=True,
                                size="lg",
                                opened=False 
                            ),
                            dmc.Modal(
                                id=page+'-modal_tipe2',
                                title="Notification",
                                children=[],
                                centered=True,
                                size="lg",
                                opened=False 
                            ),
                            dmc.Button(
                                "Submit",
                                id=page+ 'submit-btn',
                                variant="outline",
                                className='mt-4',
                                style={'fontSize': '12px', 'padding': '4px 8px', "width": "100%"}
                            ),
                        ],
                        span=6
                    )
                   ],
            ),
        ], style={'left': "10%", 'width': "80%", 'justify-content': 'center', "position": "absolute"}),
    ], className='container',
        style={
            'justify-content': 'center',
            "position": "absolute",
            "background-color": "#ffffff",
            "top": "5%",
            "left": "25%",
            "width": "50vw",
            "min-width": "50vw",
            "height": "90%",
            "padding": "20px",
            "border-radius": "10px",
            "box-shadow": "rgba(0, 0, 0, 0.1) 0px 4px 12px",
            "overflow-y": "scroll",
        }),

], id=page+ '_Master')


@callback(
    Output(page+ 'asset_code', 'value'),
    Input(page+ 'asset_type', 'value'),
    prevent_initial_call=True
)
def update_asset_code(asset_type):
    if asset_type:
        # Placeholder for DB engine (hidden for confidentiality)
        engine = create_engine('your_connection_string_here')

        # Simulated query for last asset code of given type
        query = f"SELECT asset_code FROM assets_table WHERE asset_type = '{asset_type}' ORDER BY asset_code DESC LIMIT 1"
        data = pd.read_sql_query(query, engine)

        if data.empty:
            asset_code = f"{1:04d}"
        else:
            asset_code = f"{int(data['asset_code'].iloc[0][-4:]) + 1:04d}"

        return f"{asset_type}{asset_code}"

    return ""


@callback(
    Output(page+ 'submit-btn', 'disabled'),
    Output(page+ 'submit-btn', 'children'),
    Output(page+ 'submit-btn', 'color'),
    Output(page+'-modal_tipe1', 'opened'),
    Output(page+'-modal_tipe1', 'children'),
    Output(page+'-modal_tipe2', 'opened'),
    Output(page+'-modal_tipe2', 'children'),
    Input(page+ 'submit-btn', 'n_clicks'),
    State(page+ 'asset_item_type', 'value'),
    State(page+ 'asset_item_code', 'value'),
    State(page+ 'asset_item_name', 'value'),
    State(page+ 'asset_item_brand', 'value'),
    State(page+ 'asset_item_size', 'value'),
    State(page+ 'asset_item_price', 'value'),
    State(page+ 'asset_item_discount', 'value'),
    State(page+ 'asset_item_note', 'value'),
    prevent_initial_call=True
)
def save_asset_to_db(n_clicks, asset_type, asset_code, asset_name, asset_brand, asset_size, asset_price, asset_discount, asset_note):
    if n_clicks:
        if not (asset_type and asset_code and asset_name and asset_brand and asset_size and asset_price):
            return False, "Please fill in all required fields", "red"

        asset_lastupdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        asset_activeyn = 'Y'
        asset_userid = current_user.username  # placeholder for authenticated user

        # Placeholder connection string (hidden for confidentiality)
        engine = create_engine('your_connection_string_here')

        with engine.connect() as conn:
            insert_query = text("""
                INSERT INTO asset_items (
                    item_type, item_code, item_name, item_brand, item_unitsize, 
                    item_price, item_discount, item_note, item_activeyn, item_userid, item_lastupdate
                )
                VALUES (
                    :item_type, :item_code, :item_name, :item_brand, :item_unitsize,
                    :item_price, :item_discount, :item_note, :item_activeyn, :item_userid, :item_lastupdate
                )
            """)

            conn.execute(insert_query, {
                "item_type": asset_type,
                "item_code": asset_code,
                "item_name": asset_name,
                "item_brand": asset_brand,
                "item_unitsize": asset_size,
                "item_price": asset_price,
                "item_discount": asset_discount,
                "item_note": asset_note,
                "item_activeyn": asset_activeyn,
                "item_userid": asset_userid,
                "item_lastupdate": asset_lastupdate
            })

        return False, "Submit", "blue"



@callback(Output(page + '-url', "href"),
          Input(page + '-modal_tipe2', 'opened'),
          prevent_initial_call=True)
def reload_page(n_clicks):
    if n_clicks:
        return "/item-asset"
    return no_update

# Optional: set specific React version (advanced, not required)
# dash._dash_renderer._set_react_version("18.2.0")

if __name__ == "__main__":
    app = dash.Dash(__name__, external_stylesheets=[dmc.styles.DATES], suppress_callback_exceptions=True)
    app.layout = dmc.MantineProvider(children=layout)
    app.run_server(debug=True)

