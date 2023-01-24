import { AxiosResponse } from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next'
const axios = require('axios');

type ResponseData = {
  number ?: Number
  error ?: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  axios.get(process.env["BACKEND_URL"] + "/numeral-to-number?numeral=" + req.query.numeral).then(
      (response : AxiosResponse) => {

          if (response.data.number) {
            console.log(response.data.number)
            res.status(200).json({number: response.data.number})
          } else {
            console.log(response.data.error)
            res.status(200).json({error: response.data.error})
          }
          
      }
  )
  
}
