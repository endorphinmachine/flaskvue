module.exports={
  assetsDir: "static",//放置静态资源的目录
  publicPath: "./",//基本路径
  devServer: {
    hot: true,
    open: true,
    disableHostCheck: true,
    proxy: {
      "": {
        target: "http://127.0.0.1:5000/",
        ws: true,
        changeOrigin: true, //开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        pathRewrite: {
            '^': '' //这里理解成用''代替target里面的地址
          }
      }
    }
  }  
}