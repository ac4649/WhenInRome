import { Box, Text } from "grommet"
import react from "react"

// We deal with converting the underscores to overlines here
interface IShowUpperBars {
    value: string
}

const ShowUpperBars = ( props : IShowUpperBars) => {
    let hasUpperBar = false
    return (
        <Box direction="row">
            {
                props.value.split("").map(
                    (cur_value, index) => {
                        if (cur_value == "_") {
                            hasUpperBar = true
                            return null
                        }

                        if (hasUpperBar) {
                            hasUpperBar = false
                            return (
                                <Text key={index} style={{textDecoration: "overline"}}>
                                    {cur_value}
                                </Text>
                            )
                        } else {
                            return (
                                <Text key={index}>
                                    {cur_value}
                                </Text>
                            )
                        } 
                
                    }
                )
            }
        </Box>
    )

}

export default ShowUpperBars
export { ShowUpperBars as ShowUpperBars}