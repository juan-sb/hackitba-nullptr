import axios from "axios";

const _axios = axios.create({
  withCredentials: true,
  crossDomain: true
});

if (process.env.NODE_ENV !== 'production') {
  _axios.defaults.baseURL = "http://127.0.0.1:8000"
}
_axios.defaults.xsrfCookieName = 'csrftoken'
_axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export default _axios;
