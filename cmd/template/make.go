package template

import (
	"fmt"

	"github.com/spf13/cobra"
)

var makeCmd = &cobra.Command{
	Use:   "make",
	Short: "Create a new project based on the template",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("make called")
	},
}

func init() {
	TemplateCmd.AddCommand(makeCmd)
}
