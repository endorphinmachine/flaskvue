//根据不同的环境更改不同的baseUrl
let baseUrl = '';
 
//开发环境下
if (process.env.NODE_ENV == 'development') {
    baseUrl = 'http://localhost:8000';
 
} else if (process.env.NODE_ENV == 'production') {
    baseUrl = 'http://127.0.0.1:5000';
}
 
export {
    baseUrl,//导出baseUrl
}