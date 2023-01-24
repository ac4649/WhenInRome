import { AxiosError, AxiosResponse } from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next'
const axios = require('axios');

type ResponseData = {
  number ?: Number
  error ?: string
}

export const config = {
  api: {
    responseLimit: false,
  },
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {

  try {
    let response = await axios.get(process.env["BACKEND_URL"] + "/numeral-to-number?numeral=" + req.query.numeral)
    if (response.data.number) {
      res.status(200).json({number: response.data.number})
    } else {

      if (response.status == 200) {
        res.status(200).json({error: response.data.error})
      } else {
        res.status(200).json({error: "An Unknown Error Occured"})
      }
      
    }
  
  } catch (error) {
    res.status(200).json({error: "An Unknown error occured"})
  }
  
}
