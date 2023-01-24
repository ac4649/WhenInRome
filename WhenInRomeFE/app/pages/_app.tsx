import '@/styles/globals.css'
import { Grommet, grommet } from 'grommet'
import { deepMerge } from 'grommet/utils';
import type { AppProps } from 'next/app'

const theme = deepMerge(grommet, {
  global: {
      colors: {
          brand: '#3c5ccf',
          primary: '#3c5ccf',
      },
  },
  formField: {
    requiredIndicator: true,
    label: {
        weight:"bold",
        color:'primary',
        requiredIndicator: true,
    }
  }
})

export default function App({ Component, pageProps }: AppProps) {
  return (
    <Grommet full theme={theme}>
      <Component {...pageProps} />
    </Grommet>
  )
}
