#coding=utf-8
SPREADSHEET_KEY 	=	'1YYrHsejzTj1sbwCx5hIKupQkVMisa-Cu3iuk4f-apU8'  #   key of the spreadsheet
SITE_NAME           =   u'Calvin+Suzie'                                 #   Title of the website !
GIVE				=	u'Give'                                         #   Label for the button on the wishlit
ALREADY_GIVEN		=	u'Alreay given'                                 #   Label for items already given on the wishlit
DETAILS				=	u'details'                                      #   Label for the link on the wishlist

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INFO_LINK           =   u"Info"             # the display name the info page
INFO_PAGE           =   u"""
    <h1 class="cover-heading">Informations</h1>

    <p class="lead">
        Default text for the information page. Here you can put pictures, links, planning details,
        contact info and whatnot. Emphasis can be achieved throught <span class="bold shadowed">bold shadowed</span>.
    </p>
    <br>

    <!-- You can also add a carousel ... -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.4.1/holder.js"></script>
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel" style="width:660px;margin:auto;">
        <!-- Indicators -->
        <ol class="carousel-indicators">
            <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
            <li data-target="#carousel-example-generic" data-slide-to="1"></li>
            <li data-target="#carousel-example-generic" data-slide-to="2"></li>
        </ol>

        <!-- Wrapper for slides -->
        <div class="carousel-inner" role="listbox">
            <div class="item active">
                <img src="holder.js/660x495/sky/text:First image" alt="First">
                <div class="carousel-caption capt">
                    First image : caption
                </div>
            </div>
            <div class="item">
                <img src="holder.js/660x495/vine/text:Second image" alt="Second">
                <div class="carousel-caption capt">
                    Caption for second image
                </div>
            </div>
            <div class="item">
                <img src="holder.js/660x495/lava/text:Last image" alt="Last">
                <div class="carousel-caption capt">
                    Third and last caption
                </div>
            </div>
        </div>

        <!-- Controls -->
        <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    <br>
    <p class="lead">
        Have fun editing this !
    </p>
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HONEYMOON_LINK      =   u"Honeymoon"                # the display name the honeymoon page.
                                                    # If None, no honeymoon page will be displayed.

HONEYMOON_PAGE      =   u"""
    <h1 class="cover-heading">Honeymoon</h1>

    <p class="lead">
        Default text for the honeymoon page. Here you can put pictures, links, planning details,
        contact info and whatnot. Emphasis can be achieved throught <span class="bold shadowed">bold shadowed</span>.
    </p>
    <br>
    <p class="lead">
        Have fun editing this !
    </p>
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ACCOMMODATION_LINK  =   u"Housing"                  # the display name the Accommodation page.
                                                    # If None, no Accommodation page will be displayed.

# Header to display before the accomodation list
ACCOMMODATION_HEADER =  u"""
    <h1 class="cover-heading">Accommodation</h1>

    <p class="lead">
        Default header for the accommodation page. Here you can put pictures, links, planning details,
        contact info and whatnot. Emphasis can be achieved throught <span class="bold shadowed">bold shadowed</span>.
        <br>
        <br>
        The accommodation list will be shown after this text.
    </p>
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WISHLIST_LINK   =   u"Wishlist"                     # the display name the wishlist page.
                                                    # If None, no wishlist page will be displayed.


# Header to display before the wishlist
WISHLIST_HEADER     =   u"""
    <h1 class="cover-heading">Wishlist</h1>

    <p class="lead">
        Default header for the wishlist page. Here you can put pictures, links, planning details,
        contact info and whatnot. Emphasis can be achieved throught <span class="bold shadowed">bold shadowed</span>.
        <br>
        <br>
        The wishlist will be shown after this text.
    </p>
"""
