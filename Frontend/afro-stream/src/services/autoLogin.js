 function autoLogin() {
 console.log("merchantAppId", merchantAppId);
 getMiniAppToken().then(token => {
 //2. Verify the returned token of the Super APP. If the token is verified, login is not required.
 authToken(token);
 }).catch(ex => {
 }).finally(() => {
 });
 }
 //1.get token from Super app
 function getMiniAppToken() {
 return new Promise((resolve, reject) => {
 window.ma.native("getMiniAppToken", {appId: merchantAppId}).then(res =>
{
 console.log("res", res);
 let data = JSON.parse(res);
 resolve(data.token);
 }).catch(ex => {
 reject(ex);
 });
 });
 }
 // 3.call H5 service auth token and get userinfo
 function authToken(token) {
 let loading = weui.loading('loading', {});
 window.fetch(baseUrl + "/auth/token", {
 method: "post",
 headers: {
 'Content-Type': 'application/json'
 },
 body: JSON.stringify({
 authToken: token
 })
 }).then(res => {
 res.json().then(json => {
   console.log(json);
   let biz = json.biz_content;
 let openId = biz.open_id;
 let identityId = biz.identityId;
 console.log(openId);
 document.getElementById('userinfo').innerHTML =
 `openId: <br> <span style='color:red;'>${openId}</span>
 <br>
 identityId: <br> <span style='color:red;'>${identityId}</span>`;
 });
 }).finally(() => {
 loading.hide();
 })
 }
