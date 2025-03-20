import axios from 'axios'
import { ElMessage } from 'element-plus'

const api = axios.create({
  baseURL: 'http://localhost:3000/api',
})

api.interceptors.request.use(
  config => {
    config.headers.Authorization =
      'Bearer fastgpt-fxGsKfzZzq1cKvx0Mj6mXJyWGyqLtb6PkWkMpCZUoJnvldStuBK9687RWbx'
    return config
  },
  error => {
    ElMessage.error(error)
    return Promise.reject(error)
  },
)

export default api
