/*
	Any misc client side only javascript
*/

/**
 * Sets up the 'Authorities' Page
 */
function showAuths() {
    $("#authTitle").text("AUTHORITIES");
    $("#infoText").text("The search bar filters items by the authority name, geographic focus, and owner.");
    $("#detail_table").toggle();
    $("#certsSearch").toggle();
    $("#authsSearch").toggle();
    $("#main_table").toggle();
		$("#viewButton").hide();
		$("#exportButton").hide();
    $("#authName").hide();
    $("#back_button").hide();
    $("#delete").hide();
    $("#editTrustButton").hide();
    $("#footer").attr("id", "footer_plain");
}

/**
 * Searches the table of authorities on the 'Authorities' page for
 * the given input and hides rows that do not contain that value.
 * Currently allows searching for general name, country of origin, or the owner of the cert
 * @param {String} inputVal - The value to search for
 */
function searchMainTable(inputVal)
{
    $('#main_table > tbody > .parent').each(function(index, row)
    {
        var allCells = $(row).find('td:nth-child(2)');	//The general list of authorities
        var countryCell = $($($(row).siblings('.child-' + $(row).attr('id'))[1]).children()[2]);	//The cells that contain the country of origin of the authority
        var ownerCell = $($($(row).siblings('.child-' + $(row).attr('id'))[2]).children()[2]);		//The cells that contain the owner of the authority
        allCells.push(countryCell);
        allCells.push(ownerCell);
        if(allCells.length > 0)
        {
            var found = false;
            allCells.each(function(index, td)
            {
                var regExp = new RegExp(inputVal, 'i');		//case insensitive RegEx to look for searched value
                if(regExp.test($(td).text()))
                {
                    found = true;
                    return;
                }
            });
            if(found === true) {
                $(row).show();
                $('#spacer-' + $(row).attr('id')).show();
            }
            else {
                $(row).hide();                
                $(row).addClass('parentClosed');
                $(row).removeClass('parentOpen');
                $(row).siblings('.child-' + $(row).attr('id')).hide();
                $('#spacer-' + $(row).attr('id')).hide();
            }
        }
    });
}

/**
 * Searches the table of certificates on the 'Certificates' page 
 * for the given input and hides rows that do not contain that value.
 * @param {String} inputVal - The value to search for
 */
function searchDetailTable(inputVal)
{
    $('#detail_table > tbody > .parent').each(function(index, row)
    {
        var allCells = $(row).find('td:nth-child(1)');		//The names of all the certs in the table
        if(allCells.length > 0)
        {
            var found = false;
            allCells.each(function(index, td)
            {
                var regExp = new RegExp(inputVal, 'i');		//case insensitive RegEx to look for searched value
                if(regExp.test($(td).text()))
                {
                    found = true;
                    return false;
                }
            });
            if(found === true)
                $(row).show();
            else
            {
                $(row).hide();
                $(row).siblings('.child-' + $(row).attr('id')).hide();
            }
        }
    });
}