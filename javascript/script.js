document.getElementById("side_bar").onmouseover = function() {
            document.getElementById("buy_coin_text_id").innerHTML = " Buy Coin";
            document.getElementById("live_price_text_id").innerHTML = " Live price";
            document.getElementById("tutorial_text_id").innerHTML = " Tutorial";
            document.getElementById("Account_text_id").innerHTML = "Account";
        }
document.getElementById("side_bar").onmouseout = function() {
            document.getElementById("buy_coin_text_id").innerHTML = " ";
            document.getElementById("live_price_text_id").innerHTML = " ";
            document.getElementById("tutorial_text_id").innerHTML = " ";
            document.getElementById("Account_text_id").innerHTML = " ";
        }
        var n=0;
function Invalid_email(){
    document.getElementById("invalid_email").innerHTML="<spam class='invalid_massage'>Invalid Email</spam>";
        document.getElementById("login_box").style.width="400px";
}
function Invalid_password(){
    document.getElementById("invalid_password").innerHTML="<spam class='invalid_massage'>Invalid password</spam>";
        document.getElementById("login_box").style.width="400px";
}