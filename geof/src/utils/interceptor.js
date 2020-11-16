import axios from 'axios'
import { baseURL } from './env.js'
// 创建axios实例
const service = axios.create({
  baseURL: baseURL,
  timeout: 180000,
  crossDomain: true,//设置cross跨域
  withCredentials: true//设置cross跨域 并设置访问权限 允许跨域携带cookie信息
});

service.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
// 请求拦截器： 在浏览器发送请求之前的处理; 用处：发送请求之前可以判断：是否合法，是否符合请求参数的要求
service.interceptors.response.use(
  (config) => {
      //拦截请求，做统一处理
      console.log('请稍后');
      console.log(config);
      return config
  },
  (error) => {
  return Promise.reject(error) 
})

// 响应拦截器： 服务器返回数据后处理
service.interceptors.response.use(
  (response) => {
      //拦截响应，做统一处理
      console.log('数据请求成功');
      console.log(response);
      const res = response.data
      return res
  },
  (error) => {
  return Promise.reject(error.response.status) // 返回接口返回的错误信息
})
// 对外暴露接口
export default service