def css():
    print("""
        <style>
            body {
                background-color: white;
                margin: 0;
                padding: 0;
                font-family: 'Arial';
            }

            a{
                color: #333436;
                text-decoration: none;
            }

        """)

    nav_bar()
    home_shop()
    list()

    print("""
        </style>
        """)


def home_shop():
    print("""

    #shop-screen{
        display: flex;
        flex-wrap: wrap;
        width: 75vw;
        float: right;
        margin-right: 2vw;
        margin-top: 5vh;
    }

    .shop-item{
        border: #D9DBDB 2px solid;
        box-shadow: 2px 3px 5px #C0C0C0;
        width: 150px;
        height: 350px;
        margin: 10px;
        flex-basis: 275px;
        text-align: center;

    }

    .shop-item-image{
        height: 200px;
    }

    .shop-item-name{
        font-size: 20px;
        line-height: 2vh;
        height: 40px;
    }

    .shop-item-appelation{
        font-size: 13px;
        line-height: 10px;
    }

    .shop-item-informations-button{
        margin-top: 10px;
        background-color: #3E8ED0;
        width: 50%;
        color: white;
        font-size: 13px;
        border-radius: 3px;
        margin-left: 25%;
        height: 30px;
        line-height: 30px;
    }

    #shop-filters-screen{
        display: flex;
        flex-direction: row;
    }

    #filters-screen{
        width: 20vw;
        height: 50vh;
        margin-top: calc(5vh + 10px);
        box-shadow: 2px 3px 5px #C0C0C0;
        padding-top: 10px;
    }

    #filter-form-submit{
        border: none;
        margin-top: 10px;
        background-color: #9AD06E;
        width: 50%;
        color: white;
        font-size: 13px;
        border-radius: 3px;
        margin-left: 25%;
        height: 30px;
        float: bottom;
        line-height: 30px;
    }

    .filter-form-input{
        width: 15vw;
        margin-left: 2.5vw;
        height: 30px;
    }
    """)


def nav_bar():
    print("""
    #navbar{
        display: flex;
        flex-direction: row;
        height: 55px;
        color: #303030;
        padding: 20px;  
        font-weight: bold;
    }

    #project-name{
        font-size: 20px;
        width: 200px;
        margin-left: 2vw;

    }

    .navbar-item{
        font-size: 15px;
        margin-left: 1vw;
        width: 100px;
        text-align: center;
        margin-top: 10px;
    }

    .navbar-item:hover{
        text-decoration: underline 2px black;
    }

    #edit-button{
        margin-left: 68vw;

    }   

        """)


def list():
    print("""
    .list-item{
        width: 80vw;
        height: 5vh;
        line-height: 5vh;
        border: 1px solid #E7E7E7;
        font-family: 'Arial';
        padding-top: 0.5vh;

    }

    .list-item-buttons{
        float: right;
        display: flex;
        flex-direction: row;
    }

    .list-item-button{
        border: none;
        border-radius: 2px;
        color: white;
        padding: 10px;
        height: 5vh;
        float: right;
        margin-top: -5vh;
    }

    #list-item-modify{
        background-color: #3E8ED0;
        margin-right: 1vw;
    }

    #list-item-delete{
        background-color: #F14668;
    }



    """)