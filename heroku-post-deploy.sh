echo $HEROKU_APP_NAME
echo "postdeploy"
export CLIENT_HOST=https://$HEROKU_APP_NAME.herokuapp.com
