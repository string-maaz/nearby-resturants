$(document).ready(function() {
        processGeoLocation()
});


(function($) {
    var ajaxCall = function(that, url, type, data, successHandler, errorHandler, xhrHandler) {
        // console.log('ajaxCall', data);
        $.ajax({
            type: type,
            url: url,
            data: data,
            contentType: false,
            processData: false,
            success: function(response) {
                if (errorHandler) {
                    if (response.status == 'SUCCESS')
                        successHandler(that, response)
                    else
                        errorHandler(that, response)
                } else
                    successHandler(that, response)
            },
            xhr: function() {
                var xhr = new window.XMLHttpRequest();

                if (xhrHandler) {

                    xhr.addEventListener("loadstart", function(event) {
                        xhrHandler(that);
                    }, false);

                }
                return xhr;
            },
            error: function(error) {
                console.error(error)
            }
        })
    }

    var getCookie = function(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie).replace(/ /g, '');
        var cookies_list = decodedCookie.split(';');
        for (var i = 0; i < cookies_list.length; i++) {
            cookie = cookies_list[i].split('=')
            if (cookie[0] == cname)
                return cookie[1]
        }
        return "";
    }

    processGeoLocation = function() {
        navigator.geolocation.getCurrentPosition(geoSuccess, geoError, { enableHighAccuracy: false, maximumAge: 10000, timeout: 10000 });
    }


    var geoSuccess = function(position) {
        startPos = position;
        console.log(startPos.coords.latitude, startPos.coords.longitude);
        data = {
            lat: startPos.coords.latitude,
            lng: startPos.coords.longitude,
            // csrfmiddlewaretoken: getCookie('csrftoken'),
            isGeoDataAvailable: true,
        }
        console.log(data)
        ajaxCall(this, '/location/process-user-place/', 'get', window.location.search.substr(1) + "&" + $.param(data), geoSavedSuccess, geoSavedError)
    };
    
    
    var geoError = function(error) {
        data = {
            // csrfmiddlewaretoken: getCookie('csrftoken'),
            isGeoDataAvailable: false,
        }
        if(typeof fetching_special_type_posts != 'undefined' && fetching_special_type_posts != false){
            data['post']=fetching_special_type_posts;
        }
        ajaxCall(this, '/location/process-user-place/', 'get', window.location.search.substr(1) + "&" + $.param(data), geoSavedSuccess, geoSavedError)
    }

    var geoSavedSuccess = function(that, responseData) {
        //do nothing
    }


    var geoSavedError = function(that) {
        // console.error("Goecode error")
    }


    var putAutocomplete = function($element, contextData) {
        $element.ng_autocomplete({
            url: '/suggestions/',
            contextData: contextData,
            select: function($element, item) {
                $element.attr('data-id', item.id);
                // console.log("selected item ", item.label, item.id);
            },
            unselect: function($element) {
                $element.attr("data-id", null);
            }

        });
    }


})(jQuery)