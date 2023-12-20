package cmd

import (
	"os"

	"devg/cmd/template"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "devg",
	Short: "A developers everyday work tool",
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	rootCmd.AddCommand(template.TemplateCmd)
	rootCmd.CompletionOptions.DisableDefaultCmd = true
}
