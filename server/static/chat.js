// Copyright 2009 FriendFeed
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

function newMessage ($form) {
    var message = $form.formToDict(),
        $submitButton = $form.find("input[type=submit]")
    ;    
    $submitButton.disable();
    
    $.postJSON("/a/message/new", message, function (response) {
        updater.showMessage(response);
        if (message.id) {
            form.parent().remove();
        } 
        else {
            form.find("input[type=text]").val("").select();
            $submitButton.enable();
        }
    });
}

function getCookie (name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

jQuery.postJSON = function (url, args, callback) {    
    args._xsrf = getCookie("_xsrf");
    $.ajax({
        url: url, 
        data: $.param(args), 
        dataType: "text", 
        type: "POST",
        success: function (response) {
            if (callback) {
                callback(eval("(" + response + ")"));
            }
        }, 
        error: function (response) {
            console.log("ERROR:", response);
        }
    });
};

jQuery.fn.formToDict = function () {
    var fields = this.serializeArray(),
        json = { };

    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }

    if (json.next) delete json.next;
    return json;
};

jQuery.fn.disable = function () {
    this.enable(false);
    return this;
};

jQuery.fn.enable = function (should_enable) {
    if (arguments.length && !should_enable) {
        this.attr("disabled", "disabled");
    } else {
        this.removeAttr("disabled");
    }
    return this;
};

var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function () {
        var args = { 
            "_xsrf" : getCookie("_xsrf") 
        };

        if (updater.cursor) {
            args.cursor = updater.cursor;
        }

        $.ajax({
            url: "/a/message/updates", 
            type: "POST", 
            dataType: "json",
            data: $.param(args), 
            success: updater.onSuccess,
            error: updater.onError
        });
    },

    onSuccess: function (json_response) {
        updater.newMessages(json_response);
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function (response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function (response) {
        var messages = response.messages;
        if (!messages) return;

        updater.cursor = response.cursor;
        updater.cursor = messages[messages.length - 1].id;
        console.log(messages.length, "new messages, cursor:", updater.cursor);
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    showMessage: function (message) {
        var node,
            existing = $("#m" + message.id)
        ;
        if (existing.length > 0) return;
        
        node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};

$(document).ready(function () {
    var $messageform = $("#messagform"),
        $message = $message
    ;

    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function () {};

    $messageform.live("submit", function () {
        newMessage($(this));
        return false;
    });

    $messageform.live("keypress", function (e) {
        if (e.keyCode == 13) {
            newMessage($(this));
            return false;
        }
    });

    $("#message").select();

    updater.poll();
});
