import { AxiosResponse } from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next'
const axios = require('axios');

type ResponseData = {
  numeral ?: string
  error ?: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  axios.get("http://127.0.0.1:8000/number-to-numeral?number=" + req.query.number).then(
      (response : AxiosResponse) => {
        if (response.data.numeral) {
          res.status(200).json({numeral: response.data.numeral})
        } else {
          console.log(response.data.error)
          res.status(200).json({error: response.data.error})
        }
          
      }
  )
  
}
