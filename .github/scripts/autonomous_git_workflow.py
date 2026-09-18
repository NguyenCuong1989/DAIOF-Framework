        self.logger.info(f"🧬 K-State: {self.k_state} | HAIOS Compliant: {report['haios_compliance']}")


def main():
    """Main entry point."""
    args = sys.argv[1:]
    single_mode = bool(args and args[0] == 'single')

    # Preserve the documented ``single <command>`` form while accepting the
    # direct ``status`` command used by health checks and tests.
    if single_mode:
        args = args[1:]

    if args and args[0] in {'status', 'cycle', 'pull', 'push'}:
        workflow = AutonomousGitWorkflow()
        command = args[0]

        if command == 'status':
            print(json.dumps(workflow.get_git_status(), indent=2))
            return

        if command == 'cycle':
            print(json.dumps(workflow.execute_workflow_cycle(), indent=2))
            return

        if command == 'pull':
            success = workflow.autonomous_pull()
        else:
            success = workflow.autonomous_push()

        if not success:
            raise SystemExit(1)
        return

    if single_mode:
        AutonomousGitWorkflow().run_continuous_workflow(interval=60)
        return

    # Run multi-repository orchestration when no single-repository command was
    # requested.
    orchestrator = MultiRepositoryOrchestrator()
    orchestrator.run_continuous_orchestration(interval=300)  # Check every 5 minutes


if __name__ == '__main__':
    main()